from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True, default=None)
    
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'))
    goal = db.relationship("Goal", back_populates="tasks")
        
    def to_dict(self):
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": (self.completed_at != None)
        }
        
    def to_dict_with_goal_id(self):
        task_dict = self.to_dict()
        if self.goal_id:
            task_dict["goal_id"] = self.goal_id
        return task_dict
            
    @classmethod
    def from_dict(cls, task_details):
        new_task = cls(
            title=task_details["title"],
            description=task_details["description"]
        )
        return new_task
    
