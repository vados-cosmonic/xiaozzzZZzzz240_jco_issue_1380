import * as process from "node:process";

import { WASIShim } from "@bytecodealliance/preview2-shim/instantiation";

import { instantiate } from "./transpiled-python/component.js";

async function main() {
    const instance = await instantiate(undefined, {
        ...(new WASIShim().getImportObject()),
    });

    // console.log("instance?", instance);

    // NOTE: this file has the *exact* same funcitonality that the
    // C++ code attempts to perform, and produces the same result
    // without crashing, when the C++ guest->guest call cannot.
    const handle = new instance['test:jco-bug/iface'].openTemp();
    handle.append("|x|");

    // // run() by itself will error regardless of jco vs wasmtime 
    // // see: run-only-error-output.txt
    // //
    // instance['wasi:cli/run@0.2.0'].run();
}

main().catch(err => {
    console.error("ERROR", err);
    process.exit(-1);
});
