import os
import http
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from router import expense_record


ROOT = os.path.dirname(__file__)
app = FastAPI(
    root_path='/pft',
    title='boostrap 網頁測試',
    # dependencies=[Depends(get_sso_user)],
    version='1.2.3',
    responses={
        # 401: {
        #     "model": ErrorResponseModel,
        #     "description": "身分驗證失敗"
        # }
    }
)

app.include_router(router=expense_record.router, tags=['收支記錄相關 API'], prefix='/expense-record')
app.mount('/index', StaticFiles(directory=os.path.join(ROOT, 'static'), html=True), name='static')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
