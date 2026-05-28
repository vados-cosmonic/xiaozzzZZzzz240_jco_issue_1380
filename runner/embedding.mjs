import * as process from "node:process";

import { WASIShim } from "@bytecodealliance/preview2-shim/instantiation";

import { instantiate } from "./transpiled/combined.js";

async function main() {
    const instance = await instantiate(undefined, {
        ...(new WASIShim().getImportObject()),
    });

    instance['wasi:cli/run@0.2.0'].run();
}

main().catch(err => {
    console.error("ERROR", err);
    process.exit(-1);
});
