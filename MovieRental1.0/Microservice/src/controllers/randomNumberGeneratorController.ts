import express from "express";
import { RandomNumberGenerator } from "../models/RandomNumberGenerator";
import { Request, Response } from "express";

const router = express.Router();

//Return an integer between the given min and max query parameters
router.get("/range", async (req: Request, res: Response) => {
  const min = req.query.min;
  const max = req.query.max;

  if (typeof min === "string" && typeof max === "string") {
    if (min > max) {
      res.status(400).send("Min should not be greater than Max");
    } else {
      const randomNumber = RandomNumberGenerator.generate(
        parseInt(min),
        parseInt(max)
      );
      res.json({ randomNumber });
    }
  } else {
    res.status(400).send("Bad Request");
  }
});

//return an integer between 1 and the given max integer parameter
router.get("/max/:maxInt", async (req: Request, res: Response) => {
  const maxInt = req.params.maxInt;

  if (typeof maxInt === "string") {
    const randomNumber = RandomNumberGenerator.generate(1, parseInt(maxInt));
    res.json({ randomNumber });
  } else {
    res.status(400).send("Bad Request");
  }
});

export default router;
