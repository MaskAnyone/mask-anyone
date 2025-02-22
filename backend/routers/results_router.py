from fastapi import APIRouter

from db.job_manager import JobManager
from db.db_connection import DBConnection
from db.result_blendshapes_manager import ResultBlendshapesManager
from db.result_mp_kinematics_manager import ResultMpKinematicsManager
from db.video_manager import VideoManager

job_manager = JobManager(DBConnection())
result_blendshapes_manager = ResultBlendshapesManager(DBConnection())
result_mp_kinematics_manager = ResultMpKinematicsManager(DBConnection())
video_manager = VideoManager(DBConnection())

router = APIRouter(
    prefix="/results",
)


@router.get("/{video_id}/all")
def get_all_results(video_id: str):
    results = video_manager.fetch_all_results(video_id)
    return {"results": results}


@router.get("/{result_video_id}/blendshapes")
def get_blendshapes(result_video_id: str):
    try:
        result_blendshapes = (
            result_blendshapes_manager.fetch_result_blendshapes_entry_by_resvid_id(
                result_video_id
            )
        )

        return result_blendshapes.data
    except Exception as error:
        return None


@router.get("/{result_video_id}/mp-kinematics")
def get_mp_kinematics(result_video_id: str):
    try:
        result_mp_kinematics = (
            result_mp_kinematics_manager.fetch_result_mp_kinematics_entry_by_resvid_id(
                result_video_id
            )
        )

        return result_mp_kinematics.data
    except Exception as error:
        return None
