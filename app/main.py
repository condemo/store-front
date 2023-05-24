import asyncio

from app import App


async def main() -> None:
    app = App()
    # TODO: Preload
    # TODO: Creation
    # TODO: Render
    app.mainloop()


if __name__ == "__main__":
    asyncio.run(main())
