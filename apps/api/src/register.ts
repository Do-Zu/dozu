import moduleAlias from 'module-alias';

// ts-node runs this from src; compiled Node runs it from dist, independently of cwd.
moduleAlias.addAliases({ '@': __dirname });
