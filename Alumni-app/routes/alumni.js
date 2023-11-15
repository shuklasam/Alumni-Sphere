const express = require("express");
const router = express.Router();

const {
  getAlumnis,
  postAlumni,
  getAlumni,
  searchAlumni,
} = require("../controllers/alumni");

router.route("/").get(getAlumnis).post(postAlumni);
router.route("/detail").get(getAlumni);
router.route("/search").get(searchAlumni);

module.exports = router;
