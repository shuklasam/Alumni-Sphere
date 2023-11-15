const mongoose = require("mongoose");

const alumniSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  about: {
    type: String,
  },
  linkedinUrl: {
    type: String,
    required: true,
  },
  imageUrl: {
    type: String,
  },
  university: {
    type: String,
    require: true,
  },
  worksAt: {
    type: String,
  },
  pastExperience: {
    type: [String],
  },
  skills: {
    type: [String],
  },
  higherStudies: {
    type: [String],
  },
});



module.exports = mongoose.model("alumni", alumniSchema);
