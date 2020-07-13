from typing import Optional
from datetime import datetime

from sqlalchemy import and_, or_

from app import db, ma


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    src = db.Column(db.String(2084), nullable=False)
    short = db.Column(db.String(10), nullable=False, unique=True, index=True)
    is_one_off = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> None:
        return "Link(id={}, src={}, short={}, is_one_off={}, created_at={}," \
            "deleted_at={})".format(
                self.id,
                self.src,
                self.short,
                self.is_one_off,
                self.created_at,
                self.deleted_at)

    def __str__(self) -> str:
        return self.src

    @property
    def expiring(self) -> bool:
        return self.deleted_at is not None

    @staticmethod
    def get_from_short(short: str) -> Optional['Link']:
        return Link.query.filter(
            and_(Link.short == short,
                 # `is` can not be overloaded,
                 # so it won't work with query builder
                 or_(Link.deleted_at == None,
                     Link.deleted_at > datetime.utcnow())
                 )).first()


class LinkSchema(ma.Schema):
    class Meta:
        fields = ("src", "short", "is_one_off", "deleted_at", "expiring")


link_schema = LinkSchema()
