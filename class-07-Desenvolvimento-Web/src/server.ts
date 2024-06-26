import express from "express";
import "dotenv/config";

const app = express();
const PORT = process.env.PORT || 3333;

app.listen(PORT, () => {
  console.log(`Server is running on PORT ${PORT}...`);
});
