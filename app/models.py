from sqlalchemy import String;
from sqlalchemy.orm import Mapped, mapped_column;
from app.database import Base;
from app.enums import JobStatus;

class Job(Base):
    __tablename__ = "jobs";

    id: Mapped[int] = mapped_column(primary_key=True);
    name: Mapped[str] = mapped_column(String(100));
    file: Mapped[str] = mapped_column(String(255));
    status: Mapped[str] = mapped_column(String(20), default=JobStatus.queued.value);