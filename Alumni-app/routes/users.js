const express = require("express");
const router = express.Router();

const { test } = require("../controllers/users");

router.route('/').get(test);

module.exports = router