from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas, database

router = APIRouter(prefix="/api/members", tags=["members"])

@router.get("/", response_model=List[schemas.Member])
def read_members(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = Query(None),
    db: Session = Depends(database.get_db)
):
    """Get all members with optional search"""
    return crud.get_members(db, skip=skip, limit=limit, search=search)

@router.get("/{member_id}", response_model=schemas.Member)
def read_member(member_id: int, db: Session = Depends(database.get_db)):
    """Get a specific member by ID"""
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@router.post("/", response_model=schemas.Member)
def create_member(member: schemas.MemberCreate, db: Session = Depends(database.get_db)):
    """Create a new member"""
    return crud.create_member(db=db, member=member)

@router.put("/{member_id}", response_model=schemas.Member)
def update_member(
    member_id: int,
    member_update: schemas.MemberUpdate,
    db: Session = Depends(database.get_db)
):
    """Update a member"""
    db_member = crud.update_member(db, member_id=member_id, member_update=member_update)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@router.get("/{member_id}/borrows")
def get_member_borrows(member_id: int, db: Session = Depends(database.get_db)):
    """Get all borrows for a specific member"""
    db_member = crud.get_member(db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    
    borrows = db_member.borrows
    return borrows