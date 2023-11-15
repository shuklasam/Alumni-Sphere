const asyncWrapper = require("../middleware/async");
const { HttpStatusCode } = require("axios");

const test = asyncWrapper(async (req, res) => {
  console.log(req.headers['API_KEY']);
  res.status(HttpStatusCode.Ok).json({
    done: "done",
  });
});

module.exports = {
  test,
};
