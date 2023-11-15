const alumni = require("../models/alumni");
const testAlumni = require("../models/user");
const asyncWrapper = require("../middleware/async");

const getAlumnis = asyncWrapper(async (req, res) => {
  const { page } = req.query;
  const perPage = 30;
  const skip = (page - 1) * perPage;
  console.log(page);

  try {
    const data = await testAlumni.find().skip(skip).limit(perPage).exec();

    res.json(data);
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
});

const getAlumni = asyncWrapper(async (req, res) => {
  const { id } = req.query;
  console.log(id);

  try {
    const data = await testAlumni.findById(id);
    res.json(data);
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Internal server error" });
  }
});

const searchAlumni = asyncWrapper(async (req, res) => {
  const { q } = req.query;
  console.log(q);

  try {
    const data = await testAlumni.find({
      $or: [
        { about: { $regex: q, $options: "i" } },
        { skills: { $regex: q, $options: "i" } },
        { pastExperience: { $regex: q, $options: "i" } },
        { higherStudies: { $regex: q, $options: "i" } },
      ],
    });

    res.json(data);
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Internal server error" });
  }
});

const postAlumni = async (req, res) => {
  try {
    const data = await testAlumni.create({
      ...req.body,
    });

    res.status(200).json({ data });
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: "Internal server error" });
  }
};

module.exports = { getAlumnis, postAlumni, getAlumni, searchAlumni };
