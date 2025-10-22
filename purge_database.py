import asyncio
from app.db import engine
from app import models  # make sure models are imported before running (models register tables)
from sqlalchemy import MetaData, text


async def truncate_all():
    """Truncate all tables in the connected database.

    This function reflects the current database metadata and issues a single
    TRUNCATE ... RESTART IDENTITY CASCADE statement against all discovered
    tables. It uses the async engine from `app.db`.
    """
    metadata = MetaData()

    async with engine.begin() as conn:
        # reflect current database schema into metadata using a sync reflection
        await conn.run_sync(metadata.reflect)

        tables = list(metadata.sorted_tables)
        if not tables:
            print("No tables found to truncate.")
            return

        def fq(table):
            # include schema if present and quote identifiers to be safe
            if table.schema:
                return f'"{table.schema}"."{table.name}"'
            return f'"{table.name}"'

        names = ', '.join(fq(t) for t in tables)
        sql = f'TRUNCATE TABLE {names} RESTART IDENTITY CASCADE;'
        print(f'Executing: {sql}')

        await conn.execute(text(sql))

    print("✅ All tables truncated.")


if __name__ == "__main__":
    warning_msg = (
        "\n❗❗❗ ⚠ Warning! ⚠ ❗❗❗\n"
        "\n"
        "You are about to delete ALL of the data\n"
        "in EVERY table in the database.\n"
        "\n"
        "Are you really sure you want to do that?\n"
        "\n"
        "Type `DELETE` to confirm.\n"
        "> "
    )
    user_input = input(warning_msg)
    if user_input.strip() != "DELETE":
        print("Aborting. No data was deleted.")
        exit(0)
    asyncio.run(truncate_all())
