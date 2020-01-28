linear_extrude(height=10, twist=120){
    union(){
        mirror([1, 0, 0]){
            union(){
                translate(v=[0, 0, 0]){
                    translate(v=[6, 4, 0]){
                        translate(v=[0.5858197940568532, -4.767126042723606, 3.1340820126468216]){
                            cylinder(h=4);
                        };
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
                        translate(v=[0.6085016237992458, 0.1995345709544849, 0.08586775879288466]){
                            cylinder(h=4);
                        };
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
                    translate(v=[0.5858197940568532, -4.767126042723606, 3.1340820126468216]){
                        cylinder(h=4);
                    };
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
                    translate(v=[0.6085016237992458, 0.1995345709544849, 0.08586775879288466]){
                        cylinder(h=4);
                    };
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
