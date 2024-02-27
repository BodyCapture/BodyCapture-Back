
import { pool } from "../../config/db.config.js";
import { BaseError } from "../../config/error";
import { status } from "../../config/response.status";
import { getAllStudioQuery } from "../models/studio.sql.js";
export async function getAllStudio() {
    try {
        const conn = await pool.getConnection();
        const [studioList] = await conn.query(getAllStudioQuery);
        conn.release();
        return studioList;
    } catch (error) {
        console.error("MySQL Connection Error:", error);
        throw new BaseError(status.PARAMETER_IS_WRONG);
    }
}