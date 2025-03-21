from sqlalchemy.orm import Session
from sqlalchemy import func

class DBUtils:
    @staticmethod
    def fetch_one(db: Session, model, **filters):
        return db.query(model).filter_by(**filters).first()

    @staticmethod
    def fetch_many(db: Session, model, limit=100, offset=0, **filters):
        query = db.query(model)
        for key, value in filters.items():
            if isinstance(value, list):
                query = query.filter(getattr(model, key).in_(value))
            else:
                query = query.filter_by(**{key: value})
        return query.limit(limit).offset(offset).all()

    @staticmethod
    def insert_one(db: Session, model_instance):
        db.add(model_instance)
        db.commit()
        db.refresh(model_instance)
        return model_instance

    @staticmethod
    def insert_many(db: Session, model_instances):
        db.add_all(model_instances)
        db.commit()
        return model_instances

    @staticmethod
    def update_one(db: Session, model, id, **updates):
        instance = db.query(model).filter(model.id == id).first()
        if instance:
            for key, value in updates.items():
                setattr(instance, key, value)
            db.commit()
            db.refresh(instance)
        return instance

    @staticmethod
    def update_many(db: Session, model, filters, **updates):
        instances = db.query(model).filter_by(**filters).all()
        for instance in instances:
            for key, value in updates.items():
                setattr(instance, key, value)
        db.commit()
        return instances

    @staticmethod
    def get_count(db: Session, model, **filters):
        return db.query(model).filter_by(**filters).count()

    @staticmethod
    def group_by(db: Session, model, group_by_column, agg_func=func.sum, agg_column=None):
        query = db.query(group_by_column, agg_func(agg_column)) if agg_column else db.query(group_by_column)
        return query.group_by(group_by_column).all()

    @staticmethod
    def join(db: Session, model, join_model, join_condition, **filters):
        return db.query(model).join(join_model, join_condition).filter_by(**filters).all()

db_utils = DBUtils()