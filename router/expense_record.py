import os
from fastapi import APIRouter, Depends, File, Form, HTTPException, Response, UploadFile, status, Query, Request
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

ROOT = os.path.dirname(__file__)
print(ROOT)
router = APIRouter()
templates = Jinja2Templates(directory='./static/templates')

@router.post('/page')
def expense_record_page(request: Request) -> HTMLResponse:
    print(os.getcwd())
    return templates.TemplateResponse('expense_record.html', {'request': request})

@router.post('/get-category')
def get_category()

# @router.post("/page")
# async def expense_record_page() -> HTMLResponse:
#     page_title = '收支記錄'
#     html = f'''
#     <section>
#       <h1>{page_title}</h1>
#       <p>This is an HTML snippet.</p>
#     </section>
#     '''
#     return HTMLResponse(content=html)