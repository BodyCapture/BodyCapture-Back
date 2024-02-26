
import { pool } from "../../config/db.config.js";
import { BaseError } from "../../config/error";
import { status } from "../../config/response.status";
import { getAllMakeupQuery } from "../models/makeup.sql.js";
export async function getAllMakeup() {
    try {
        const conn = await pool.getConnection();
        const [makeupList] = await conn.query(getAllMakeupQuery);
        conn.release();
        return makeupList;
    } catch (error) {
        throw new BaseError(status.PARAMETER_IS_WRONG);
    }
}