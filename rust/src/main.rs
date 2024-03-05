use rust_demo::{
    actions_service_client::ActionsServiceClient,
    authentication_service_client::AuthenticationServiceClient,
    configuration_service_client::ConfigurationServiceClient, GetMinerConfigurationRequest,
    LoginRequest, PauseMiningRequest, ResumeMiningRequest,
};

use tokio::time::{sleep, Duration};
use tonic::{
    metadata::{Ascii, MetadataMap, MetadataValue},
    Extensions,
};

use std::env;
use std::io;

async fn login(
    addr: &str,
    user: &str,
    pass: &str,
) -> Result<MetadataValue<Ascii>, Box<dyn std::error::Error>> {
    let mut client = AuthenticationServiceClient::connect(addr.to_string()).await?;

    let request = tonic::Request::new(LoginRequest {
        username: user.into(),
        password: pass.into(),
    });

    let response = client.login(request).await?;

    Ok(response.metadata().get("authorization").unwrap().clone())
}

async fn get_miner_config(addr: &str, map: MetadataMap) -> Result<(), Box<dyn std::error::Error>> {
    let mut client = ConfigurationServiceClient::connect(addr.to_string()).await?;

    let request =
        tonic::Request::from_parts(map, Extensions::default(), GetMinerConfigurationRequest {});

    let response = client.get_miner_configuration(request).await?;

    println!("current miner config: {:#?}", response.get_ref());

    Ok(())
}

async fn pause_resume_miner(
    addr: &str,
    map: MetadataMap,
) -> Result<(), Box<dyn std::error::Error>> {
    let mut client = ActionsServiceClient::connect(addr.to_string()).await?;

    let pause_request =
        tonic::Request::from_parts(map.clone(), Extensions::default(), PauseMiningRequest {});
    let resume_request =
        tonic::Request::from_parts(map, Extensions::default(), ResumeMiningRequest {});

    println!("Trying to pause mining for 30s");
    let _ = client.pause_mining(pause_request).await?;

    sleep(Duration::from_secs(30)).await; // Asynchronously sleep for 30 seconds

    println!("Trying to resume mining");
    let _ = client.resume_mining(resume_request).await?;

    println!("All good!");

    Ok(())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = env::args().nth(1).expect("Please, provide an address");

    println!("Enter username:");
    let mut username = String::new();
    io::stdin().read_line(&mut username)?;

    println!("Enter password:");
    let mut password = String::new();
    io::stdin().read_line(&mut password)?;

    let auth_token = login(&addr, username.trim(), password.trim()).await?;

    let mut metadata = MetadataMap::new();
    metadata.insert("authorization", auth_token);

    get_miner_config(&addr, metadata.clone()).await?;
    pause_resume_miner(&addr, metadata).await?;

    Ok(())
}
