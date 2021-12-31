def register_theater_route(api, app, prefix='api'):
    from .controllers import theater

    api.add_namespace(theater, path=f'/{prefix}/theater/')
