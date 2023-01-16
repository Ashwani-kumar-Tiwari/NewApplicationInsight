# import logging

# from opencensus.ext.azure.log_exporter import AzureLogHandler
# from opencensus.ext.azure.trace_exporter import AzureExporter
# from opencensus.trace import config_integration
# from opencensus.trace.samplers import ProbabilitySampler
# from opencensus.trace.tracer import Tracer

# config_integration.trace_integrations(['logging'])

# logger = logging.getLogger(__name__)

# handler = AzureLogHandler(connection_string='<Your Connection String>')
# handler.setFormatter(logging.Formatter('%(asctime)s %(traceId)s %(spanId)s %(message)s'))
# logger.addHandler(handler)

# tracer = Tracer(
#     exporter=AzureExporter(connection_string='<Your Connection String>'),
#     sampler=ProbabilitySampler(1.0)
# )

# logger.warning('Before the span')
# with tracer.span(name='Hello'):
#     logger.warning('In the span')
# logger.warning('After the span')