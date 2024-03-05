use walkdir::WalkDir;

use std::path::PathBuf;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let protos: Vec<PathBuf> = WalkDir::new("../bos-plus-api/proto/")
        .into_iter()
        .filter_map(|e| e.ok())
        .filter(|e| e.path().extension() == Some("proto".as_ref()))
        .inspect(|p| println!("{}", p.path().display()))
        .map(|e| e.path().to_owned())
        .collect();

    tonic_build::configure().compile(&protos, &["../bos-plus-api/proto/"])?;
    Ok(())
}