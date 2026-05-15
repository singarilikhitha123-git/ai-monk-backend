from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Any
import models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TreePayload(BaseModel):
    tree: Any


@app.get("/trees")
def get_trees(db: Session = Depends(get_db)):
    trees = db.query(models.Tree).order_by(models.Tree.created_at).all()
    return [{"id": t.id, "tree": t.tree} for t in trees]


@app.post("/trees")
def create_tree(payload: TreePayload, db: Session = Depends(get_db)):
    tree = models.Tree(tree=payload.tree)
    db.add(tree)
    db.commit()
    db.refresh(tree)
    return {"id": tree.id, "tree": tree.tree}


@app.put("/trees/{tree_id}")
def update_tree(tree_id: int, payload: TreePayload, db: Session = Depends(get_db)):
    tree = db.query(models.Tree).filter(models.Tree.id == tree_id).first()
    if not tree:
        raise HTTPException(status_code=404, detail="Tree not found")
    tree.tree = payload.tree
    db.commit()
    db.refresh(tree)
    return {"id": tree.id, "tree": tree.tree}
