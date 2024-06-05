import json
from typing import Optional, List

from supabase import Client as SupabaseClient

from model.jobs import JobOpening
from .supa import DBClient

class JobDB(DBClient):

    def __init__(self, supabase: SupabaseClient):
        super().__init__(supabase)
        self.table_name = "job_openings"

    def fetch_jobs(self, owner_id: str) -> Optional[List[JobOpening]]:
        results: Optional[List[JobOpening]] = None
        if self.connection is not None:
            dict_results = self.connection.table(self.table_name).select("*").eq("owner", owner_id).execute().data
            if dict_results is not None and len(dict_results) > 0:
                results = [JobOpening(**job) for job in dict_results]
        return results

    def create_job(self, owner_id: str, job: JobOpening) -> Optional[JobOpening]:
        if self.connection is not None:
            result = None
            job.owner = owner_id
            data = job.model_dump_json(exclude={'id'},
                                       include={
                                           'title',
                                           'company',
                                           'description',
                                           'location',
                                           'job_type',
                                           'work_mode',
                                           'hiring_manager',
                                           'keywords',
                                           'owner',
                                           'url'
                                       })
            try:
                result = self.connection.table(self.table_name).insert(json.loads(data)).execute()
            except Exception as e:
                print(f"Create job failed: {e}")
            if result is not None and len(result.data) > 0:
                return JobOpening(**result.data[0])
        return job

    def update(self, job: JobOpening) -> Optional[JobOpening]:
        if self.connection is not None:
            result = None
            data = job.model_dump_json(
                include={
                    'id',
                    'title',
                    'company',
                    'description',
                    'location',
                    'job_type',
                    'work_mode',
                    'hiring_manager',
                    'keywords',
                    'owner',
                    'url'
                }
            )
            try:
                result = self.connection.table(self.table_name).update(json.loads(data)).eq('id', job.id).execute()
                print(f'Job saved: {result}')
            except Exception as e:
                print(f"Update job failed: {e}")
            if result is not None and len(result.data) > 0:
                return JobOpening(**result.data[0])
        return job

    def delete(self, job: JobOpening) -> None:
        if self.connection is not None:
            try:
                self.connection.table(self.table_name).delete().eq('id', job.id).execute()
            except Exception as e:
                print(f"Delete job failed: {e}")