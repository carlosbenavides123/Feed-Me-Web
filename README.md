# feedme

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# Backend

Build the project.
- (sudo) docker build .

Run the unit tests (will download all dependencies from requirements if havn't done so yet)
- (sudo) docker-compose run --rm app sh -c "python manage.py test && flake8"

Add new migrations (assuming new model has been made, core is a directory for example)
- (sudo) docker-compose run --rm app sh -c "python manage.py makemigrations core"
