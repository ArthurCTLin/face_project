# Face Project – Face Cropping & Recognition

This project provides facial image processing and recognition tools via both **Command Line Interface (CLI)** and **RESTful API**, supporting:

- **Face Cropping**: Automatically detects and extracts all faces from an image.
- **Face Matching**: Searches a face image database to find whether a specific person appears.

---

## Project Structure
<pre>face_project/
├── api/                    # FastAPI server (REST API)
│   └── main.py
├── face_search/            # Core functions
│   ├── __init__.py
│   ├── face_cropper.py     # Face cropping logic
│   └── face_matcher.py     # Face matching logic
├── face_tool.py            # CLI entry point
├── requirements.txt
├── README.md
└── .gitignore</pre>

## Installation
1. Create environment
   ```bash
   $ conda create -n <env_name> python=3.8
   $ conda activate <env_name>
   ```
2. Clone repository
   ```bash
   $ git clone https://github.com/ArthurCTLin/face_project.git
   $ cd face_project/
   ```
3. Install deppendencies
   ```bash
   $ pip install -r requirements.txt
   ```
## Implementation
### CLI
1. Crop faces from a single image
   ```bash
   $ python face_tool.py crop ./data/sample.jpg
   ```
   $\qquad \qquad \qquad \qquad \qquad \qquad$<img src="https://github.com/user-attachments/assets/0928c05e-33ce-4721-a12b-b202c59b8b70" width=50%>
   
   $\qquad \qquad \qquad \qquad$<img src="https://github.com/user-attachments/assets/af847bf3-734a-421a-80aa-1d0b24b142d8" width=70%>

3. Match a target face with stored faces
   Compares the target face with faces stored in the ./storage directory and prints matched results with distances.
   ```bash
   $ python face_tool.py match ./target/target_face.jpg --storage ./storage
   ```
   ![image](https://github.com/user-attachments/assets/536d5479-5f7d-4e66-bb26-a8f4b16e987e)

### Run on API
  ```bash
  $ uvicorn api.main:app --host 0.0.0.0 --port 8001 --reload
  ```
  * `POST /crop/`
  Upload a single image and crop all detected faces.
  
  * `POST /crop_batch/`
  Upload multiple images and crop all faces in each image.
  
  * `POST /match/`
  Upload a target face image and compare it with a specified folder of face images.

***◎ All photos are sourced from the internet.***

## Todo
* [ ] Support .zip upload for batch processing
* [ ] Basic frontend interface (image upload + preview)
* [ ] Dockerize the API for deployment
