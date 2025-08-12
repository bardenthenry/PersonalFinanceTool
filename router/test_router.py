from fastapi import APIRouter, Depends, File, Form, HTTPException, Response, UploadFile, status, Query
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse

router = APIRouter()