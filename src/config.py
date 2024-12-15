import dataclasses

from environs import Env
from sqlalchemy import URL


@dataclasses.dataclass(frozen=True, slots=True)
class DbConfig:
    host: str
    password: str
    user: str
    database: str
    port: int
    naming_convention = {
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s',
    }

    @staticmethod
    def from_env(env: Env) -> 'DbConfig':
        host = env.str('DB_HOST')
        password = env.str('POSTGRES_PASSWORD')
        user = env.str('POSTGRES_USER')
        database = env.str('POSTGRES_DB')
        port = env.int('DB_PORT', 5432)

        return DbConfig(
            host=host,
            password=password,
            user=user,
            database=database,
            port=port,
        )

    @property
    def construct_sqlalchemy_url(
        self,
        driver: str = 'asyncpg',
        host: str | None = None,
        port: int | None = None,
    ) -> str:
        if not host:
            host = self.host
        if not port:
            port = self.port
        uri = URL.create(
            drivername=f'postgresql+{driver}',
            username=self.user,
            password=self.password,
            host=host,
            port=port,
            database=self.database,
        )
        return uri.render_as_string(hide_password=False)

    @property
    def construct_psql_dns(self) -> str:
        uri = URL.create(
            drivername='postgresql',
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )
        return uri.render_as_string(hide_password=False)


@dataclasses.dataclass(frozen=True, slots=True)
class Config:
    db: DbConfig
