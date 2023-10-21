# IndeedJobSearch

I realized manually searching for jobs on **Indeed** was ineffective and wasting too much time so I created an **Indeed** scraper. Running **_main.py_** takes user input for _job_ and _location_, then writes to csv file to make the job hunt more efficient. I also removed any job post that was unwilling to list pay details ("$") in description because those jobs are annoying. Check out **Example** folder for an example of the scrape. Good luck, I hope this helps you!

# Get Started

1. Download **_main.py_** 
2. Create virtual environment by opening command prompt:
   * >pip install virtualenv
   * >virtualenv myenv
   * >myenv\Scripts\activate  # On Windows
      * OR
    * >source myenv/bin/activate  # On MacOS or Linux
3. Install dependencies on virtualenv
    * >pip install selenium
4. Download **chromedriver**
5. From command promp virtualenv, CD into directory where you saved **_main.py_**
6. Run file
    * >python **_main.py_** 
7. Open _jobs.csv_ in Excel or Google Sheets

# Other Nonessential Details

* Indeed scraper takes _job_ input and _location_ input from command prompt. Feel free to leave _location_ empty and it will return more jobs.
* Indeed scraper returns information while scraping such as:
  * _Page 1 processed. Total jobs collected so far: 8._
  * _Page 2 processed. Total jobs collected so far: 20._
  * _Page 3 processed. Total jobs collected so far: 30._
* Indeed scraper will prompt you after 10 pages collected:
  * Yes will continue for another 10 pages then ask you again. No will stop.
  * _Processed 10 pages. Would you like to continue? (yes/no):_
* Implicit waits are included because load times vary. Please be patient.
