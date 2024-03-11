import express from "express";
import randomNumberGeneratorController from "../controllers/randomNumberGeneratorController";

const router = express.Router();

router.use("/random", randomNumberGeneratorController);

export default router;