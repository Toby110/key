import tornado.ioloop
import asyncio
import url
import config

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app=url.make_app()
    app.listen(config.options['port'])
    tornado.ioloop.IOLoop.current().start()
