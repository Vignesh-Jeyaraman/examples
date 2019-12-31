class LambdaBase(object):
	"""
	LambdaBase handler class. This class is required to make our serverless code class based.
    We will be calling the get_handler method from our app which will call our handle function.
	"""
	@classmethod
	def get_handler(cls, *args, **kwargs):
		def handler(event, context):
			return cls(*args, **kwargs).handle(event, context)
		return handler

	def handle(self, event, context):
		raise NotImplementedError

