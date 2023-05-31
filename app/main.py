import asyncio

from app import App


async def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    asyncio.run(main())
