
import Home from "@material_plugin/views/Home";


// Navigation
const navigation = {
    "__home": Home, // Plugin Homepage
    "__plugin_nav": [
        {
            name: "Material UI Plugin Group",
            items: [
                {
                    "name": "Material UI Plugin",
                    "path": "material-ui",
                    "model": "plugin:material_ui.material"
                }
            ]
        }
    ],
}


export { navigation }

