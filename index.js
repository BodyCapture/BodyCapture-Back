// app.js
import express from 'express';
import makeupRoutes from './src/routes/makeup.route.js';
import pool from './config/db.connect';

const app = express();
const port = 3000;

// 여기에서 pool을 사용할 수 있습니다.

app.use(makeupRoutes);

app.listen(port, () => {
  console.log(`서버가 http://localhost:${port} 포트에서 실행 중입니다.`);
});
