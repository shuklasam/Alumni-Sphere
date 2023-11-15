const express = require("express");
const app = express();

const connectDB = require("./db/connect");
require("dotenv").config();
const helmet = require("helmet");
const cors = require("cors");
const xss = require("xss-clean");

const alumni = require("./routes/alumni");

app.use(express.json());
app.use(helmet());
app.use(cors());
app.use(xss());
app.set("trust proxy", 1);

app.get("/", async (req, res) => {
  res.send("Site seems fine");
});

app.use("/api/v1/alumni", alumni);

const port = process.env.PORT || 5000;

const start = async () => {
  try {
    const uri = process.env.MONGO_URI;
    await connectDB(uri);
    app.listen(port, console.log(`server is listening on ${port}...`));
  } catch (error) {
    console.log(error);
  }
};

start();
