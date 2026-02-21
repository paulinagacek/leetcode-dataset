import requests
import pandas as pd
import os
import re
import time
from datetime import datetime
from pathlib import Path

class LeetCodeVoteScraper:
    def __init__(self, cutoff_date_str="2022-11-30"):
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Origin": "https://leetcode.com",
            "Referer": "https://leetcode.com/"
        }
        self.output_dir = "human_medium"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Konwersja daty granicznej (sprzed ChatGPT)
        self.cutoff_date = datetime.strptime(cutoff_date_str, "%Y-%m-%d")
        self.failed_tasks = []

    def extract_python_code(self, content):
        """Wyciąga kod Pythona i wymusza obecność 'def' oraz 'return'"""
        if not content: return None
        content = content.replace('\\n', '\n').replace('\\t', '\t')
        
        patterns = [
            r'```(?:python3?|py)(.*?)\n(.*?)```',
            r'```\n(.*?)```',
            r'```(.*?)```'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                groups = match.groups()
                code = groups[-1] if len(groups) > 1 else groups[0]
                code = code.strip()
                # Dekodowanie znaków specjalnych
                code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
                
                
                if "def " in code and "return " in code:
                    return code
        return None

    def run(self, title_slug, problem_id_str, target_count):
        folder_name = f"{problem_id_str}-{title_slug}"
        task_dir = os.path.join(self.output_dir, folder_name)

        # Sprawdzenie czy zadanie już jest gotowe
        if os.path.exists(task_dir):
            existing_files = [f for f in os.listdir(task_dir) if f.endswith('.txt')]
            if len(existing_files) >= target_count:
                print(f"--- [{problem_id_str}] {title_slug} - POMINIĘTO (gotowe: {len(existing_files)}) ---")
                return

        os.makedirs(task_dir, exist_ok=True)
        print(f"\n--- Zadanie: [{problem_id_str}] {title_slug} ---")

        self.headers["Referer"] = f"https://leetcode.com/problems/{title_slug}/solutions/"

        query = """
        query communitySolutions($questionSlug: String!, $skip: Int!, $first: Int!, $orderBy: TopicSortingOption, $languageTags: [String!]) {
          questionSolutions(
            filters: {questionSlug: $questionSlug, skip: $skip, first: $first, orderBy: $orderBy, languageTags: $languageTags}
          ) {
            solutions {
              id
              post {
                creationDate
                voteCount
                content
              }
            }
          }
        }
        """

        saved_count = 0
        skip = 0
        batch_size = 40
        
        # ZMIANA: oldest_to_newest błyskawicznie znajduje stare zadania sprzed 2022
        while saved_count < target_count and skip < 400:
            variables = {
                "questionSlug": title_slug,
                "skip": skip,
                "first": batch_size,
                "orderBy": "oldest_to_newest", 
                "languageTags": ["python", "python3"] 
            }

            try:
                r = self.session.post("https://leetcode.com/graphql", json={"query": query, "variables": variables}, headers=self.headers)
                data = r.json()
                
                if 'errors' in data:
                    print(f"  [!] Błąd GraphQL: {data['errors'][0]['message']}")
                    break
                    
                solutions = data.get('data', {}).get('questionSolutions', {}).get('solutions', [])
                if not solutions: break 

                for sol in solutions:
                    if saved_count >= target_count: break

                    post = sol.get('post')
                    if not post: continue

                    ts = post['creationDate']
                    creation_dt = datetime.fromtimestamp(ts)

                    # Filtr daty
                    if creation_dt > self.cutoff_date:
                        continue 

                    clean_code = self.extract_python_code(post['content'])

                    if clean_code:
                        date_str = creation_dt.strftime('%Y-%m-%d')
                        # Format nazwy: 0003-longest-substring...-2020-07-19_1.txt
                        filename = f"{folder_name}-{date_str}_{saved_count + 1}.txt"
                        path = os.path.join(task_dir, filename)
                        
                        if not os.path.exists(path):
                            with open(path, "w", encoding="utf-8") as f:
                                f.write(clean_code)
                            saved_count += 1
                            print(f"  [OK] Zapisano: {filename}")

                skip += batch_size
                time.sleep(0.4) 

            except Exception as e:
                print(f"  [!] Błąd pętli: {e}")
                break

        if saved_count == 0:
            self.failed_tasks.append(f"[{problem_id_str}] {title_slug} -> BRAK ROZWIĄZAŃ (def+return) przed {self.cutoff_date.date()}")

    def save_failed_report(self):
        report_filename = "_scrapping_report.txt"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"Raport scrapowania: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==================================================\n")
            for item in self.failed_tasks:
                f.write(item + "\n")
        print(f"\n[INFO] Raport zapisany w: {report_filename}")

if __name__ == "__main__":
    CSV_FILE = "leetcode_problems.csv"
    PROMTPS_DIR = Path("prompts")
    
    if not os.path.exists(CSV_FILE):
        print(f"Błąd: Nie znaleziono pliku {CSV_FILE}")
        exit()

    try:
        df = pd.read_csv(CSV_FILE)
        
        # Filtry z Twojego skryptu
        if "paidOnly" in df.columns:
            df = df[df["paidOnly"].astype(str).str.lower() == "false"]
        if "hasSolution" in df.columns:
            df = df[df["hasSolution"].astype(str).str.lower() == "true"]
<<<<<<< HEAD
            
        print(f"Załadowano {len(df)} zadań z CSV.")
        
        scraper = LeetCodeVoteScraper(cutoff_date_str="2022-11-30")

        for index, row in df.iterrows():
            title_slug = row.get("titleSlug")
            q_id = row.get("frontendQuestionId")
            
            if pd.isna(q_id): 
                q_id = row.get("questionId", "0")
            
            question_id = str(int(q_id)) if isinstance(q_id, (int, float)) else str(q_id)
            
            if title_slug:
                scraper.run(title_slug, question_id, target_count=10)
                time.sleep(0.8)

        scraper.save_failed_report()
=======
        
        if "difficulty" in df.columns:
            df = df[df["difficulty"].astype(str).str.lower() == "medium"]
        
        slugs = df['titleSlug'].to_list()[150:200]
            
        print(f"Załadowano {len(slugs)} zadań do przetworzenia.")

        for idx, file_name in enumerate(sorted(os.listdir(PROMTPS_DIR))):
            slug = file_name[5:-4]
            if slug not in slugs:
                continue
        
            scraper = LeetCodeVoteScraper()

            try:
                question_id = file_name[:4]
                scraper.run(slug, question_id, target_count=50)
                
                time.sleep(1) 

            except Exception as e:
                print(f"!!! Błąd krytyczny przy przetwarzaniu wiersza {question_id}: {e}")
                scraper.failed_tasks.append(f"WIERSZ CSV {question_id} -> CRITICAL ERROR: {e}")
                continue
            
            scraper.save_failed_report()
>>>>>>> upstream/master
                
    except Exception as e:
        print(f"Krytyczny błąd programu: {e}")