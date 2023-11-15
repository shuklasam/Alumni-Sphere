const notFound = (req, res) =>
  res.status(404).send(`The page you are trying to look does not exist`);

module.exports = notFound;
