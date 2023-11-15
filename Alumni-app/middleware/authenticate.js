const user = require('../models/User')
const jwt = require('jsonwebtoken')
const {
	UnauthenticatedError
} = require('../errors')
const {
	createCustomError
} = require('../errors/custom-error')


const auth = async (req, res, next) => {
	const apiKey = req.headers['API_KEY'];

	if (!apiKey) {
		throw new UnauthenticatedError('Authentication failed')
	}
	const appApiKey = authHeader.split(' ')[1]
	try {
		const payload = jwt.verify(token, process.env.JWT_SECRET)
		req.user = {
			userId: payload.userId,
			name: payload.name
		}
		next()
	} catch (error) {
		return next(createCustomError(`Some error`, 400))
	}
}

module.exports = auth