import asyncio
import aiosqlite

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.cursor() as cursor:
            await cursor.execute("SELECT * FROM users")
            result = await cursor.fetchall()
            print("All Users:")
            for row in result:
                print(row)
            return result


async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.cursor() as cursor:
            await cursor.execute("SELECT * FROM users WHERE age > ?", (40,))
            result = await cursor.fetchall()
            print("Users Older than 40:")
            for row in result:
                print(row)
            return result


async def fetch_concurrently():
    # Run both queries concurrently
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return all_users, older_users


# Run the async function using asyncio.run
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())