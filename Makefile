up:
	pushd redshift && docker-compose up -d && popd
	pushd airflowA && docker-compose up -d && popd
	pushd airflowB && docker-compose up -d && popd

down:
	pushd redshift && docker-compose down -v && popd
	pushd airflowA && docker-compose down -v && popd
	pushd airflowB && docker-compose down -v && popd