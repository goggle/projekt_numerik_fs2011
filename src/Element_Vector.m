function [b_el, b_el_dz1, b_el_dz2] = Element_Vector(t, p, el, z1, z2)

	r = 0.05;
	f = @(x,y,w,z) (10*exp(- ((x-w).^2 + (y-z).^2 )/r^2));
	
	x1 = p(:, 1); 
	x2 = p(:, 2);

	% Eckpunkte des Elements 
	p0 = [x1(t(el, 1)); x2(t(el, 1))]; 
	p1 = [x1(t(el, 2)); x2(t(el, 2))];
	p2 = [x1(t(el, 3)); x2(t(el, 3))];
	mid_point = (p0 + p1 + p2)/3;

	% Jacobian:
	J_el = [p1-p0 p2-p0];
	area_el = 0.5 * abs(det(J_el));
	f_mid = f(mid_point(1), mid_point(2), z1, z2);
	b_el = 1/3 * f_mid * area_el * ones(3, 1);

	f_dz1 = f(mid_point(1), mid_point(2), z1, z2) * 2/(r^2)*(mid_point(1) - z1);
	f_dz2 = f(mid_point(1), mid_point(2), z1, z2) * 2/(r^2)*(mid_point(2) - z2);

	b_el_dz1 = f_dz1 * 1/3 * area_el * ones(3, 1);
	b_el_dz2 = f_dz2 * 1/3 * area_el * ones(3, 1);

end

