linear_extrude(height=10, twist=120){
    union(){
        mirror([1, 0, 0]){
            union(){
                translate(v=[0, 0, 0]){
                    translate(v=[6, 4, 0]){
                        cylinder(h=2);
                    };
                };
                translate(v=[10, 0, 0]){
                    difference(){
                        square(size=10);
                        translate(v=[1, 1, 0]){
                            square(size=8);
                        };
                    };
                };
                translate(v=[20, 0, 0]){
                    translate(v=[6, 4, 0]){
                        cylinder(h=2);
                    };
                };
                translate(v=[30, 0, 0]){
                    difference(){
                        square(size=10);
                        translate(v=[1, 1, 0]){
                            square(size=8);
                        };
                    };
                };
            };
        };
        union(){
            translate(v=[0, 0, 0]){
                translate(v=[6, 4, 0]){
                    cylinder(h=2);
                };
            };
            translate(v=[10, 0, 0]){
                difference(){
                    square(size=10);
                    translate(v=[1, 1, 0]){
                        square(size=8);
                    };
                };
            };
            translate(v=[20, 0, 0]){
                translate(v=[6, 4, 0]){
                    cylinder(h=2);
                };
            };
            translate(v=[30, 0, 0]){
                difference(){
                    square(size=10);
                    translate(v=[1, 1, 0]){
                        square(size=8);
                    };
                };
            };
        };
    };
};
