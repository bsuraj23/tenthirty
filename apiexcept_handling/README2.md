## Run
1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Start server:
   ```powershell
   uvicorn main:app --reload
   ```
3. Use a tool like curl or Postman to POST JSON to `/items/`.
