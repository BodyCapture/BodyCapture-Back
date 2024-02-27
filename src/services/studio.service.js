import { pool } from "../../config/db.config.js";
import { BaseError } from "../../config/error";
import { status } from "../../config/response.status";
import { getAllStudioQuery } from "../models/studio.sql.js";

export async function getAllStudio() {
    const conn = await pool.getConnection();
    const [studioList] = await conn.query(getAllStudioQuery);
    conn.release();
    return studioList;
}