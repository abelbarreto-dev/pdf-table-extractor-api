# PDF Table Extractor API

API that take a pdf file and extract those found table. It take the pdf file and extract those tables, then you can your
output between excel file or a simple csv.

## Dependencies
All projects dependencies are at [requirements.txt](requirements.txt) file, but you must now:

- This project works on Python3.11.x or earlier.

I created a [Dockerfile](Dockerfile) that makes containization to deploy at an online server. I've chosen [Render](https://render.com/).

## Installation
- Dependencies:
> ```pip install -r requirements.txt```

## Project Structure
```commandline
src/
├──controller/
├──core/
├──├──data_frame/
├──exception/
├──route/
├──service/
├──util/
├──wrapper/
tests/
├──mocks/
app.py
...
```

## How To Run?
Once dependencies installed, you must run the file [app.py](app.py) to run locally.

Command to Run:
> ```python app.py```

If you wish, you can run our unittests too just typing:
> ```pytest```

---
That's all Folks!
