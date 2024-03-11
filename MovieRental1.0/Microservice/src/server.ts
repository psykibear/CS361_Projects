import routes from "./routes";
import express from 'express';

const app = express();
const port = 3050;

app.use("/api", routes);

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});