from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path

from app.core.pydantic_models import LoginUser, RegistryUser


router = APIRouter()
